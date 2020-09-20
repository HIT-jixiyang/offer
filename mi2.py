# 3 0.3
# 50.0 51.0 180.0 200.0 0.9
# 48.0 53.0 170.0 210.1 0.8
# 200.0 51.0 242.1 81.0 0.7
import numpy as np
[n,th]=list(map(float,input().strip().split(' ')))
n=int(n)
M=[]

for i in range(n):
    M.append(list(map(float,input().strip().split(' '))))
def nms(b_boxes, th):
    if len(b_boxes) == 0:
        return None
    bboxes = np.array(b_boxes)
    x1 = bboxes[:, 0]
    y1 = bboxes[:, 1]
    x2 = bboxes[:, 2]
    y2 = bboxes[:, 3]
    scores = bboxes[:, 4]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    rank = np.argsort(scores)
    result_boxes = []
    while rank.size > 0:
        index = rank[-1]
        result_boxes.append(b_boxes[index])
        x1_1 = np.maximum(x1[index], x1[rank[:-1]])
        y1_1 = np.maximum(y1[index], y1[rank[:-1]])
        x2_2 = np.minimum(x2[index], x2[rank[:-1]])
        y2_2 = np.minimum(y2[index], y2[rank[:-1]])
        w = np.maximum(0.0, x2_2 - x1_1 + 1)
        h = np.maximum(0.0, y2_2 - y1_1 + 1)
        w_h = w * h
        ious = w_h / (areas[index] + areas[rank[:-1]] - w_h)
        right= np.where(ious < th)
        rank = rank[right]
    return result_boxes
result=nms(M,th)
for res in result:
    print(' '.join(map(str,res)))


