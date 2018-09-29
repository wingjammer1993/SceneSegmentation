import main

if __name__ == '__main__':

	new_args1 = main.modify_arguments()
	new_args1.dataset_dir = r'/projects/amra8468/CamVid_Norm'
	print(new_args1)
	main.main_script(new_args1)


