import torch


def _one_hot(seg_mask, num_class):
        # transform segmentation mask into one-hot mask
        # shape: (N, H, W) -> (N, C, H, W)
        input_shape = tuple(seg_mask.shape)  # (N, H, W)
        new_shape = (input_shape[0], num_class) + input_shape[1:]
        one_hot = torch.zeros(new_shape).to(seg_mask.device, dtype=float)
        result = one_hot.scatter_(1, seg_mask.unsqueeze(1).long().data, 1.0)
        return result


def cal_metrics(gt_list: torch.Tensor, pred_list: torch.Tensor, num_class=21):
    '''
    Ignore background by default
    gt_list [N, H, W]
    pred_list [N, H, W]
    eps is used for numerical stability
    '''
    # calculate oa
    eps = 1e-5
    N_c = 0
    N_a = 0

    gt_list_onehot = _one_hot(gt_list, num_class)
    pred_list_onehot = _one_hot(pred_list, num_class)

    # ignore background
    gt_list_onehot = gt_list_onehot[:, 1:, :, :]
    pred_list_onehot = pred_list_onehot[:, 1:, :, :]

    N_c = torch.sum(torch.mul(gt_list_onehot, pred_list_onehot)).item()
    N_a = gt_list[gt_list != 0].numel()

    print((N_c + eps))
    print((N_a + eps))
    oa = (N_c + eps) / (N_a + eps)
    
    # calculate aa
    sub_acc = 0
    sub_pe = 0
    for i in range(gt_list_onehot.shape[1]):
        sub_correct = torch.sum(torch.mul(gt_list_onehot[:, i, :, :], pred_list_onehot[:, i, :, :]))
        sub_samples = gt_list_onehot[:, i, :, :]
        sub_samples = sub_samples[sub_samples != 0].numel()
        sub_acc += ((sub_correct + eps) / (sub_samples + eps))

        sub_pred = pred_list_onehot[:, i, :, :]
        sub_pred = sub_pred[sub_pred != 0].numel()
        sub_pe += (sub_samples * sub_pred)

    aa = sub_acc / gt_list_onehot.shape[1]

    # calcualte k
    pe = (sub_pe + eps) / ((N_a * N_a) + eps)
    k = (oa - pe) / (1 - pe)

    return oa, aa, k
