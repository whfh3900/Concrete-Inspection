import argparse


def parse_opts():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--crop_size',
	'-s',
        default=224,#  result_use_third_v2
        type=int,
	required=False,
        help='crop size')
    parser.add_argument(
        '--crop_inputpath',
        default='/media/deepinspection/EXD_02/csun/cd10/gurder_cut/',#  result_use_third_v2
        type=str,
	required=False,
        help='crop inputpath/example default) = /media/deepinspection/EXD_02/csun/cd10/')  
    parser.add_argument(
        '--preprocesstype',
	'-p',
        default='folder',#  result_use_third_v2
        type=str,
	required=False,
        help='choice [folder, image]') 
    parser.add_argument(
        '--makelist_inputpath',
        default='/media/deepinspection/EXD_02/csun/cd10/gurder_cut/gurder_cutcrop224',#  result_use_third_v2
        type=str,
	required=False,
        help='makelist_inputpath/example default) = /media/deepinspection/EXD_02/csun/cd10/') 
    parser.add_argument(
        '--makelist_name',
	'-n',
        default='gurderlist.txt',#  result_use_third_v2
        type=str,
	required=False,
        help='makelist_name') 
    
    args = parser.parse_args()

    return args
