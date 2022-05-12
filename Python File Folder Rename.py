import os

os.chdir('E:\Blender\Blend My NFT\Export\Blend_My_NFTs Output\Complete_Collection\Cardano_metaData')

print(os.getcwd())

for f in os.listdir():
   f_name, f_ext =os.path.splitext(f)
  
   print(f_ext)
   
   new_name ='{}{}'.format(f_name, ".metadata")

   os.rename(f, new_name)

  
