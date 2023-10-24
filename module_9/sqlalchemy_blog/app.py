import contextlib
from collections.abc import Sequence
from fastapi import FastAPI, HTTPException, Query, Depends, status
from database import create_all_tables, get_async_session
from schemas import PostBase, PostRead, PostCreate, PostPartialUpdate, CommentRead, CommentCreate, CommentBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import Base, Post, Comment


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI()


async def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0), ) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return skip, capped_limit


async def get_post_or_404(id: int, session: AsyncSession = Depends(get_async_session)) -> Post:
    select_query = select(Post).where(Post.id == id)
    result = await session.execute(select_query)
    post = result.scalar_one_or_none()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post


@app.get("/posts", response_model=list[PostRead])
async def list_posts(pagination: tuple[int, int] = Depends(pagination),
                     session: AsyncSession = Depends(get_async_session), ) -> Sequence[Post]:
    skip, limit = pagination
    select_query = (
        select(Post).options(selectinload(Post.comments)).offset(skip).limit(limit)
    )
    result = await session.execute(select_query)
    return result.scalars().all()


@app.get("/posts/{id}", response_model=PostRead)
async def get_post(post: Post = Depends(get_post_or_404)) -> Post:
    return post


@app.post("/posts", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(post_create: PostCreate,
                      session: AsyncSession = Depends(get_async_session)) -> Post:
    post = Post(**post_create.model_dump(), comments=[])
    session.add(post)
    await session.commit()
    return post


@app.patch("/posts/{id}", response_model=PostRead)
async def update_post(post_update: PostPartialUpdate, post: Post = Depends(get_post_or_404),
                      session: AsyncSession = Depends(get_async_session), ) -> Post:
    post_update_dict = post_update.model_dump(exclude_unset=True)
    for key, value in post_update_dict.items():
        setattr(post, key, value)
    session.add(post)
    await session.commit()
    return post


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post: Post = Depends(get_post_or_404),
                      session: AsyncSession = Depends(get_async_session), ):
    await session.delete(post)
    await session.commit()


@app.post("/posts/{id}/comments", response_model=CommentRead,
          status_code=status.HTTP_201_CREATED, )
async def create_comment(comment_create: CommentCreate, post: Post = Depends(get_post_or_404),
                         session: AsyncSession = Depends(get_async_session),) -> Comment:
    comment = Comment(**comment_create.model_dump(), post=post)
    session.add(comment)
    await session.commit()
    return comment
