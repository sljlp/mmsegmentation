# optimizer
optimizer = dict(type='SGD', lr=0.00, momentum=0.9, weight_decay=0.0005)
optimizer_config = dict()
# learning policy
lr_config = dict(policy='poly', power=0.9, min_lr=0, by_epoch=False)
# runtime settings
runner = dict(type='IterBasedRunner', max_iters=40000)
checkpoint_config = dict(by_epoch=False, interval=200)
evaluation = dict(interval=200, metric='mIoU', gpu_collect=False)
