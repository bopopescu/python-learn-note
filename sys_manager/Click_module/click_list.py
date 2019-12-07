import click
'''
    在几个固定选项中选择内容
'''
@click.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
def digest(hash_type):
    click.echo(hash_type)

if __name__ == '__main__':
    digest()
