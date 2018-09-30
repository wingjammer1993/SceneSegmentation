import main

if __name__ == '__main__':

	new_args1 = main.modify_arguments()
	new_args1.dataset_dir = r'C:\Users\Amruta\Desktop\Project\Datasets\CamVid_Norm'
	new_args1.color_space = "GS"
	print(new_args1)
	main.main_script(new_args1)


