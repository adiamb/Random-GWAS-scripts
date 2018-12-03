import random
import argparse
import datetime
dttime=datetime.datetime.now().strftime ("%Y%m%d")
parser = argparse.ArgumentParser(description='A script to randomize sample selection for a big GWAS cohort')
parser.add_argument('-LIST', required=True, help='list of IDS one per line file that contains the IDs')
parser.add_argument('-NO', required=True, help='Number of individuals to randomly select')
### parse the arguments
args=parser.parse_args()
famfile = args.FAM
num_ind = int(args.NO)


def main(famfile, num_ind):
	fam_dic = {}
	n = 0
	with open(famfile) as infile:
		for line in infile:
			if 'FAM' not in line: ### unrelated individuals only
				n += 1
				fam_dic[n] = line
		print('PARSED IDS FROM {} INDIVIDUALS'.format(n))

	if num_ind <= n:
		raise ValueError('Number of Individuals input is much greater than N in the dataset')
	#num_ind = 5000
	rand_sample = random.sample(fam_dic.keys(), num_ind)
	out_rand_sample=[fam_dic.get(i) for i in rand_sample if i in fam_dic]
	make_outf = open(famfile.replace('.fam', '_RANDOM_'+str(num_ind)+'.txt'), 'w')
	for item in out_rand_sample:make_outf.write(item)
	make_outf.close()

if __name__ == '__main__':main(famfile=famfile, num_ind=num_ind)
