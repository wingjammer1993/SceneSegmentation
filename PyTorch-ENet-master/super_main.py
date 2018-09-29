import main


if __name__ == '__main__':

	# new_args = main.modify_arguments()
	# new_args.dataset_dir = r'/projects/amra8468/CamVid_Norm_m20'
	# print(new_args)
	# main.main_script(new_args)

	new_args = main.modify_arguments()
	new_args.dataset_dir = r'/projects/amra8468/CamVid_Norm_m10'
	print(new_args)
	main.main_script(new_args)

	# new_args = main.modify_arguments()
	# new_args.dataset_dir = r'/projects/amra8468/CamVid'
	# print(new_args)
	# main.main_script(new_args)
	#
	# new_args = main.modify_arguments()
	# new_args.dataset_dir = r'/projects/amra8468/CamVid_Norm_p10'
	# print(new_args)
	# main.main_script(new_args)
	#
	# new_args = main.modify_arguments()
	# new_args.dataset_dir = r'/projects/amra8468/CamVid_Norm_p20'
	# print(new_args)
	# main.main_script(new_args)

