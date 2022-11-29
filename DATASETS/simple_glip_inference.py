import torch


coco_results = torch.load(
    "/workspace/GLIP/RESULTS/eval/glip_tiny_model_o365_goldg/inference/coco_2017_val/coco_results.pth"
)
predictions = torch.load(
    "/workspace/GLIP/RESULTS/eval/glip_tiny_model_o365_goldg/inference/coco_2017_val/predictions.pth"
)
print(type(coco_results))
print(type(predictions))
