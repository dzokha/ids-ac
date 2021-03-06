"""empty message

Revision ID: 605996bba076
Revises: feb4febf7fec
Create Date: 2021-09-30 03:26:17.006441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '605996bba076'
down_revision = 'feb4febf7fec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abnormals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('msg', sa.String(length=200), nullable=True),
    sa.Column('classification', sa.String(length=100), nullable=True),
    sa.Column('timestamp', sa.String(length=60), nullable=True),
    sa.Column('date_time', sa.String(length=100), nullable=True),
    sa.Column('loc', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=60), nullable=True),
    sa.Column('src_ip', sa.String(length=100), nullable=True),
    sa.Column('src_port', sa.Integer(), nullable=True),
    sa.Column('dst_ip', sa.String(length=100), nullable=True),
    sa.Column('dst_port', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('protocol_type', sa.String(length=10), nullable=True),
    sa.Column('service', sa.String(length=20), nullable=True),
    sa.Column('flag', sa.String(length=10), nullable=True),
    sa.Column('src_bytes', sa.BigInteger(), nullable=True),
    sa.Column('dst_bytes', sa.BigInteger(), nullable=True),
    sa.Column('land', sa.Integer(), nullable=True),
    sa.Column('wrong_fragment', sa.Integer(), nullable=True),
    sa.Column('urgent', sa.BigInteger(), nullable=True),
    sa.Column('hot', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('srv_count', sa.Integer(), nullable=True),
    sa.Column('serror_rate', sa.Integer(), nullable=True),
    sa.Column('srv_serror_rate', sa.Integer(), nullable=True),
    sa.Column('rerror_rate', sa.Integer(), nullable=True),
    sa.Column('srv_rerror_rate', sa.Integer(), nullable=True),
    sa.Column('same_srv_rate', sa.Integer(), nullable=True),
    sa.Column('diff_srv_rate', sa.Integer(), nullable=True),
    sa.Column('srv_diff_host_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_count', sa.Integer(), nullable=True),
    sa.Column('dst_host_srv_count', sa.Integer(), nullable=True),
    sa.Column('dst_host_same_srv_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_diff_srv_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_same_src_port_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_srv_diff_host_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_serror_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_srv_serror_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_rerror_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_srv_rerror_rate', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date_time')
    )
    op.create_table('alerts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gid_sid_rev', sa.String(length=20), nullable=True),
    sa.Column('msg', sa.String(length=200), nullable=True),
    sa.Column('classification', sa.String(length=100), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.String(length=60), nullable=True),
    sa.Column('date_time', sa.String(length=100), nullable=True),
    sa.Column('loc', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=60), nullable=True),
    sa.Column('src_ip', sa.String(length=100), nullable=True),
    sa.Column('src_port', sa.Integer(), nullable=True),
    sa.Column('dst_ip', sa.String(length=100), nullable=True),
    sa.Column('dst_port', sa.Integer(), nullable=True),
    sa.Column('meta_data', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date_time')
    )
    op.create_table('snorts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('msg', sa.String(length=200), nullable=True),
    sa.Column('classification', sa.String(length=100), nullable=True),
    sa.Column('timestamp', sa.String(length=60), nullable=True),
    sa.Column('date_time', sa.String(length=100), nullable=True),
    sa.Column('loc', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=60), nullable=True),
    sa.Column('src_ip', sa.String(length=100), nullable=True),
    sa.Column('src_port', sa.Integer(), nullable=True),
    sa.Column('dst_ip', sa.String(length=100), nullable=True),
    sa.Column('dst_port', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('protocol_type', sa.String(length=10), nullable=True),
    sa.Column('service', sa.String(length=20), nullable=True),
    sa.Column('flag', sa.String(length=10), nullable=True),
    sa.Column('src_bytes', sa.BigInteger(), nullable=True),
    sa.Column('dst_bytes', sa.BigInteger(), nullable=True),
    sa.Column('land', sa.Integer(), nullable=True),
    sa.Column('wrong_fragment', sa.Integer(), nullable=True),
    sa.Column('urgent', sa.BigInteger(), nullable=True),
    sa.Column('hot', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('srv_count', sa.Integer(), nullable=True),
    sa.Column('serror_rate', sa.Integer(), nullable=True),
    sa.Column('srv_serror_rate', sa.Integer(), nullable=True),
    sa.Column('rerror_rate', sa.Integer(), nullable=True),
    sa.Column('srv_rerror_rate', sa.Integer(), nullable=True),
    sa.Column('same_srv_rate', sa.Integer(), nullable=True),
    sa.Column('diff_srv_rate', sa.Integer(), nullable=True),
    sa.Column('srv_diff_host_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_count', sa.Integer(), nullable=True),
    sa.Column('dst_host_srv_count', sa.Integer(), nullable=True),
    sa.Column('dst_host_same_srv_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_diff_srv_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_same_src_port_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_srv_diff_host_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_serror_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_srv_serror_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_rerror_rate', sa.Integer(), nullable=True),
    sa.Column('dst_host_srv_rerror_rate', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date_time')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('snorts')
    op.drop_table('alerts')
    op.drop_table('abnormals')
    # ### end Alembic commands ###
