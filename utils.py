#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created by kai at 2018/3/22
"""
import os
import turicreate as tc


def get_similar_images(pic_path):
    dirname = "./images"
    # 加载图片库
    data = tc.image_analysis.load_images(dirname)
    data = data.add_row_number()
    images_info = list(data)

    model = tc.image_similarity.create(data)

    # tc.Image(data[0]['path']).show()
    # 查询相似的图片
    pic_info = tc.image_analysis.load_images(pic_path)
    pic_info = pic_info.add_row_number()
    similar_images = model.query(pic_info, k=10)
    # 相似图片的序号
    similar_images_info = list(similar_images)

    # 返回信息
    return_list = []
    for item in similar_images_info:
        reference_label = item["reference_label"]
        distance = item["distance"]
        rank = item["rank"]
        temp_path = images_info[reference_label]["path"]
        image_name = temp_path.split(temp_path[0])[-1]
        image_info = str(images_info[reference_label]["image"])
        return_list.append({
            "rank": rank,
            "image_info": image_info,
            "image_name": image_name,
            "distance" : distance
        })
    return return_list
