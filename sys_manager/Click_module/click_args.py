import click
"""
    接受两个参数，自动将参数转换成浮点数，并且，将两个参数以元组的形式传递给一个pos变量
"""
@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    click.echo('%s / %s' %pos)

if __name__ == '__main__':
    findme()
