import importlib

if __name__ == '__main__':

	import main
	new_args1 = main.modify_arguments()
	new_args1.dataset_dir = r'/projects/amra8468/CamVid_Norm_m20'
	print(new_args1)
	main.main_script(new_args1)

	importlib.reload(main)
	new_args2 = main.modify_arguments()
	new_args2.dataset_dir = r'/projects/amra8468/CamVid_Norm_m10'
	print(new_args2)
	main.main_script(new_args2)

	importlib.reload(main)
	new_args3 = main.modify_arguments()
	new_args3.dataset_dir = r'/projects/amra8468/CamVid'
	print(new_args3)
	main.main_script(new_args3)

	importlib.reload(main)
	new_args4 = main.modify_arguments()
	new_args4.dataset_dir = r'/projects/amra8468/CamVid_Norm_p10'
	print(new_args4)
	main.main_script(new_args4)

	importlib.reload(main)
	new_args5 = main.modify_arguments()
	new_args5.dataset_dir = r'/projects/amra8468/CamVid_Norm_p20'
	print(new_args5)
	main.main_script(new_args5)

