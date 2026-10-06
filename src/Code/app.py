from fastapi import FastAPI, HTTPException
from Code.schema import Blog

app = FastAPI()

blogs = {}

@app.get("/blogs")
def get_all_blogs():
    return blogs

@app.get("/blogs/{id}")
def get_blog(id: int):
    if id not in blogs:
        raise HTTPException(status_code=404, detail="Post not found")
    return blogs.get(id)

@app.post("/blogs")
def create_blog(blog: Blog):
    new_id = max(blogs.keys(), default=0) + 1
    new_blog = {
        "id": new_id,
        "title": blog.title,
        "content": blog.content,
        "category": blog.category,
        "tags": blog.tags
    }

    blogs[new_id] = {
        "title": blog.title,
        "content": blog.content,
        "category": blog.category,
        "tags": blog.tags
    }
    
    return new_blog

@app.put("/blogs/{id}")
def update_blog(id:int, uBlog: Blog):
    if id not in blogs:
        raise HTTPException(status_code=404, detail="Post not found")
    blogs[id] = {
        "title": uBlog.title,
        "content": uBlog,
        "category": uBlog.category,
        "tags": uBlog.tags
    }

    updated_blog = {
        "id": id,
        "title": uBlog.title,
        "content": uBlog,
        "category": uBlog.category,
        "tags": uBlog.tags,
    }

    return updated_blog

@app.delete("/blogs/{id}")
def delete_blog(id: int):
    if id not in blogs:
        raise HTTPException(status_code=404, detail="Post not found")
    del blogs[id]
    return {"message": "Post Deleted!"}