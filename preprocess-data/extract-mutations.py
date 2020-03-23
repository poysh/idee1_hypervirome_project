#!/usr/bin/python3

import csv

class NucleotideMutation:
    def __init__(self, position, original_nucleotide, mutation_nucleotide, original_id, mutation_id, country, clade):
        self.position = position
        self.original_nucleotide = original_nucleotide
        self.mutation_nucleotide = mutation_nucleotide
        self.original_id = original_id
        self.mutation_id = mutation_id
        self.country = country
        self.clade = clade

class AminoacidMutation:
    def __init__(self, position, region, original_aminoacid, mutation_aminoacid, original_id, mutation_id, country, clade):
        self.position = position
        self.region = region
        self.original_aminoacid = original_aminoacid
        self.mutation_aminoacid = mutation_aminoacid
        self.original_id = original_id
        self.mutation_id = mutation_id
        self.country = country
        self.clade = clade

def main():
    all_nucleotide_mutations = dict()
    all_aminoacid_mutations = dict()
    mutation_counts = dict()

    with open('../data/processed/tree-data.tsv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        row_i = 1
        for row in csv_reader:
            row_i += 1
            nucleotide_mutations = row['nuc'].split('-')
            aminoacid_mutations_orfs = row['mutations'].split('; ')
            aminoacid_mutations = []
            for aminoacid_mutations_orf in aminoacid_mutations_orfs:
                for idx, aminoacid_mutations_orf_mutation in enumerate(aminoacid_mutations_orf.split(', ')):
                    if idx == 0:
                        orf = aminoacid_mutations_orf_mutation.split(':')[0]
                    else:
                        aminoacid_mutations_orf_mutation = orf + ': ' + aminoacid_mutations_orf_mutation
                    aminoacid_mutations.append(aminoacid_mutations_orf_mutation)

            if (len(nucleotide_mutations), len(aminoacid_mutations)) not in mutation_counts.keys():
                mutation_counts[(len(nucleotide_mutations), len(aminoacid_mutations))] = 0
            mutation_counts[(len(nucleotide_mutations), len(aminoacid_mutations))] += 1

            for nucleotide_mutation in nucleotide_mutations:
                nucleotide_mutation = nucleotide_mutation.strip()
                if not nucleotide_mutation:
                    continue
                original_nucleotide = nucleotide_mutation[0]
                mutation_nucleotide = nucleotide_mutation[-1]
                position = int(nucleotide_mutation[1:-1])
                mutation = NucleotideMutation(position, original_nucleotide, mutation_nucleotide, row['parent'], row['name'], row['country'], row['clade'])
                all_nucleotide_mutations.setdefault(position, []).append(mutation)

            for aminoacid_mutation in aminoacid_mutations:
                aminoacid_mutation = aminoacid_mutation.strip()
                if not aminoacid_mutation:
                    continue
                aminoacid_mutation_region_and_mutation = aminoacid_mutation.split(': ')
                region = aminoacid_mutation_region_and_mutation[0]
                aminoacid_mutation = aminoacid_mutation_region_and_mutation[1]
                original_aminoacid = aminoacid_mutation[0]
                mutation_aminoacid = aminoacid_mutation[-1]
                position = int(aminoacid_mutation[1:-1])
                mutation = AminoacidMutation(position, region, original_aminoacid, mutation_aminoacid, row['parent'], row['name'], row['country'], row['clade'])
                all_aminoacid_mutations.setdefault(position, []).append(mutation)

    with open('../data/processed/tree-data-nucleotide-mutations.csv', 'w') as output_nucleotides:
        output_nucleotides.write('position,original_nucleotide,mutation_nucleotide,original_id,mutation_id, country, clade\n')
        for position, mutations in all_nucleotide_mutations.items():
            for mutation in mutations:
                output_nucleotides.write('{},{},{},{},{},{},{}\n'.format(mutation.position, mutation.original_nucleotide, mutation.mutation_nucleotide, mutation.original_id, mutation.mutation_id, mutation.country, mutation.clade))

    with open('../data/processed/tree-data-aminoacid-mutations.csv', 'w') as output_aminoacids:
        output_aminoacids.write('position,original_nucleotide,mutation_nucleotide,original_id,mutation_id, country, clade\n')
        for position, mutations in all_aminoacid_mutations.items():
            for mutation in mutations:
                output_aminoacids.write('{},{},{},{},{},{},{},{}\n'.format(mutation.position, mutation.region, mutation.original_aminoacid, mutation.mutation_aminoacid, mutation.original_id, mutation.mutation_id, mutation.country, mutation.clade))

    print('end')


if __name__ == '__main__':
    main()
