from invoke import task

@task
def start(ctx):
    ctx.run("python src/main_railway.py")