import imageio
import itertools
import os
gt_images = []
gen_images = []
input_images = []
gt_final = []
gen_final = []
source = 'data/Human_Actions/Save/Images/Default/Tests/Step_'

def convert_images_to_gif(sourceFolder):
	#sourceFolder = source + str(StepNo)
	for root, dirs, filenames in os.walk(sourceFolder):
		#print('root: ', root)
		#print('dirs: ', dirs)
		gt_images = []
		gen_images = []
		input_images = []
		gt_final = []
		gen_final = []

		newFileName = ''
		for filename in filenames:
			fullFileName = os.path.join(root,filename)

			if "input" in filename:
				#print('input')		
				input_images.append(imageio.imread(fullFileName))
			elif "gen" in filename:
				#print('gen')
				gen_images.append(imageio.imread(fullFileName))
			elif "gt" in filename:
				#print('gt')
				gt_images.append(imageio.imread(fullFileName))

		if not dirs:
			gtFileName = os.path.join(root,'ogt_GIF.gif')
			genFileName = os.path.join(root,'ogen_GIF.gif')
			originalInput = os.path.join(root,'originalInput_GIF.gif')
			#print('Original Input GIF: ', originalInput)
			#print('GT GIF: ', gtFileName)
			#print('Gen: ', genFileName)
			#gen_final = ''.join(input_images).join(gen_images)
			#gt_final = ''.join(input_images).join(gt_images)
			#print('input_images', input_images)
			#print('******************************************************')
			#print('gen_images', gen_images)
			#print('######################################################')
			gen_final = input_images + gen_images
			#print('gen_final', gen_final)
			#print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
			gt_final = input_images+gt_images
			#print('gt_final', gt_final)
			#print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
			imageio.mimsave(gtFileName, gt_final)
			imageio.mimsave(genFileName, gen_final)
			imageio.mimsave(originalInput,input_images)
		

			


def main():
	convert_images_to_gif("data/Human_Actions/img")

if __name__ == '__main__':
    main()