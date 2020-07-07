from BE import BE
from MB import MB
from Generator import Generator
import random
import time
import xlwt
from xlwt import Workbook


class Tester:

    @staticmethod
    def run(min_size, max_size, divisions, mb_size, m_arity):
        wb = Workbook()
        sheet = wb.add_sheet("results")
        method = 0
        n_size = 1
        n_arity = 2
        r_c = 3
        ms_e = 4
        r_time = 5
        delta_time = 6
        n = 0

        sheet.write(n, method, 'Method')
        sheet.write(n, n_size, 'Size')
        sheet.write(n, n_arity, 'Arity')
        sheet.write(n, r_c, 'R')
        sheet.write(n, ms_e, 'Mean-squared Error')
        sheet.write(n, r_time, 'Run Time')
        sheet.write(n, delta_time, 'Delta Time')
        n += 1

        for size in range(min_size, max_size):
            print(size)
            max_div = min(size, divisions)
            for division in range(1, max_div):
                arity = int(size * division / max_div)
                if arity < 1:
                    arity = 1
                else:
                    arity = min(arity, m_arity)
                network = Generator.create(size, arity)
                nodes = network.get_network()
                ordering = []
                for node in nodes:
                    ordering.append(node)
                random.shuffle(ordering)

                be_start = time.time()
                _, be_result = BE.solve_be(network, ordering)
                be_time = time.time() - be_start

                sheet.write(n, method, 'BE')
                sheet.write(n, n_size, size)
                sheet.write(n, n_arity, arity)
                sheet.write(n, r_time, be_time)
                n += 1

                end_mb = min(mb_size, size)
                for b_size in range(1, end_mb):
                    mb = int(arity * b_size / mb_size)
                    if mb < 1:
                        mb = 1
                    mb_start = time.time()
                    _, mb_result = MB.solve_mb(network, ordering, mb)
                    mb_time = time.time() - mb_start
                    sq_error = 0
                    for node in ordering:
                        sq_error += (be_result[node] - mb_result.get(node, 0)) ** 2
                    msq = sq_error / len(ordering)
                    d_time = be_time - mb_time

                    sheet.write(n, method, 'MB')
                    sheet.write(n, n_size, size)
                    sheet.write(n, n_arity, arity)
                    sheet.write(n, r_c, mb)
                    sheet.write(n, ms_e, msq)
                    sheet.write(n, r_time, mb_time)
                    sheet.write(n, delta_time, d_time)
                    n += 1

                    wb.save('Result.xls')


