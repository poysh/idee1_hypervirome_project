import argparse
import os
import sys

# indices (0-based) for fields to write from input
ROWS_TO_WRITE = [
    4,  # query-POS -> position (0)
    7,  # REF(hit) -> original_nucleotide (1)
    8,  # ALT(query) -> mutation_nucleotide (2)
    1,  # hit -> mutation_id (4)
]


def _check_file_exists_no_dir(file):
    """
    Check if a file does exist and is not a directory
    :param file: file to check
    :return: True or exits if file does not exist OR is a directory
    """
    if not os.path.exists(file) or os.path.isdir(file):
        sys.stderr.write("File does not exist or is a directory: %s" % file)
        exit(1)
    return True


def parse_snp_file(path_in, path_out=None, quote=None, delimiter=','):
    """
    Parses the 'blastn2snp.jar' output to hypervirome_project tree data (CSV)

    Prerequisites:
        Input file is tabular-separated
        Input file fields do not change

    :param path_in: input path to blastn2snp.jar file
    :param path_out: output file path (if None, input file path is used and file extension changed)
    :param quote: escape character for fields (output file only)
    :param delimiter: field delimiter for fields (output file only)
    :return: Nothing, writes the new file
    """

    if r"\t" in delimiter:
        delimiter = '\t'

    # create output path or check for its existence
    if path_out is None:
        path_out = '.'.join((path_in.split('.')[:-1]))
        if os.path.exists("%s.csv" % path_out):
            counter = 1
            path_out_c = "%s_%i.csv" % (path_out, counter)
            while os.path.exists(path_out_c):
                counter += 1
                path_out_c = "%s_%i.csv" % (path_out, counter)
            path_out = path_out_c
        else:
            path_out = "%s.csv" % path_out
    else:
        path_out = os.path.realpath(path_out)
        _check_file_exists_no_dir(path_out)

    # parse file
    with open(path_in) as fh_in, open(path_out, 'w') as fh_out:
        for lc, line in enumerate(fh_in):
            line = str(line).strip().split("\t")
            if lc == 0:  # get the header
                fh_out.write("%s\n" % delimiter.join(["position", "original_nucleotide",
                                                      "mutation_nucleotide", "original_id",
                                                      "mutation_id"]))
                # header = {str(name).lower(): i for i, name in enumerate(line)}
            else:  # write new line in output file
                row_to_write = [line[index] for index in ROWS_TO_WRITE]
                row_to_write.insert(3, "0")  # add "0" for 'original_id'

                if quote is not None:
                    row_to_write[-1] = '%s%s%s' % (quote, row_to_write[-1], quote)
                    # row_to_write = ['%s%s%s' % (quote, str(field), quote) for field in row_to_write]  # for all fields
                fh_out.write("%s\n" % delimiter.join(row_to_write))


if __name__ == "__main__":
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("txt_in", type=str, help="txt output of blast2snp.jar")
    parser.add_argument("-out", "-o", type=str, help="Parsed output file (Default: <input file name>.csv)",
                        default=None)
    parser.add_argument("-quote", "-q", type=str, help="Character to quote output lines (Default: No quotes)",
                        default=None)
    parser.add_argument("-delimiter", "-d", help="Delimiter for output (Default: ',' (comma))", default=',')
    args = parser.parse_args()

    file_in = os.path.realpath(args.txt_in)
    if _check_file_exists_no_dir(file_in):
        parse_snp_file(file_in, args.out, args.quote, args.delimiter)
