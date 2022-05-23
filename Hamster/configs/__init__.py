import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Deep Network Rank Analysis')
    parser.add_argument('--data', '-d', type=str, default='imagenet-val', choices=['imagenet-val', 'imagenet-val-sub', 'cifar10', 'cifar100'], help='Dataset.')
    parser.add_argument('--model', '-m', type=str, default='resnet50',
                        choices=['Lenet', 'cifar_resnet18', 'cifar_resnet34', 'cifar_resnet50', 'cifar_resnet101',
                                 'cifar_resnet152', 'resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152',
                                 'gmlpmixer_t', 'resmlp', "vit_t", "vit_s", "vit_b", "vit_l", "deit_t", "deit_s",
                                 "deit_b", "swim_t", "swim_s", "swim_b", "swim_l", "vgg11_bn", "vgg13_bn",
                                 "vgg16_bn", "vgg19_bn"], help='Network.')
    parser.add_argument('--method', type=str, default='vanilla', choices=['vanilla', 'mealv2', 'cifar100'], help='Network.')
    parser.add_argument('--wo-pretrained', action='store_true')
    parser.add_argument('--debug', action='store_true')
    # Checkpointing options
    parser.add_argument('--save', '-s', type=str, default='./results', help='Folder to save.')
    parser.add_argument('--epoch_num', '-e', type=int, default=200, help='Loading which epoch model.')
    parser.add_argument('--layers', type=str, default=None, help='Selected layers of Network.')
    parser.add_argument('--batch-size', type=int, default=128, help='Batch size.')
    parser.add_argument('--test-size', type=int, default=224, help='Test size.')
    # Acceleration
    parser.add_argument('--num-workers', type=int, default=4, help='Number of pre-fetching threads.')
    parser.add_argument('--sample-idx', type=str, default=None, help='Choose sample slice: 1,3 denotes 1,2,3.')
    parser.add_argument('--tol', type=float, default=100., help='for rank by SVD.')
    parser.add_argument('--lr', type=float, default=1e-5, help='for rank by SVD.')
    # Addition
    parser.add_argument("opts", help="Modify config options using the command-line", default=None, nargs=argparse.REMAINDER)
    return parser.parse_args()
