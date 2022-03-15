import asyncio
from bilibili_api import video
from bilibili_api import comment, sync
import pandas as pd


async def getBasicInfo(bvid):
    # 实例化 Video 类
    v = video.Video(bvid=bvid)
    # 获取信息
    info = await v.get_info()
    # 打印信息
    print(info)
    return info["aid"]


async def getAll(aid):
    # 存储评论
    comments = []
    # 页码
    page = 1
    # 当前已获取数量
    count = 0
    while True:
        # 获取评论
        c = await comment.get_comments(aid, comment.ResourceType.VIDEO, page)
        # 存储评论
        comments.extend(c['replies'])
        # 增加已获取数量
        count += c['page']['size']
        # 增加页码
        page += 1

        if count >= c['page']['count']:
            # 当前已获取数量已达到评论总数，跳出循环
            break

    # 打印评论
    comment_list = []
    for cmt in comments:
        comment_list.append([cmt['member']['uname'], cmt['content']['message']])
        print(f"{cmt['member']['uname']}: {cmt['content']['message']}")
    result = pd.DataFrame(comment_list, columns=['name', 'comments'])
    result.to_csv("../data/comments.csv", sep="\t")
    # 打印评论总数
    print(f"\n\n共有 {count} 条评论（不含子评论）")



if __name__ == '__main__':
    bvid = "BV1dP4y1g7Jo"
    aid = asyncio.get_event_loop().run_until_complete(getBasicInfo(bvid))
    sync(getAll(aid))


