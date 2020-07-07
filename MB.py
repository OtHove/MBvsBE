from Network import Network
from Node import Node
from BE import BE


class MB:

    @staticmethod
    def solve_mb(network, ordering, z):
        init_buckets = BE.bucket(network, ordering)
        elim_buckets = []
        assignment = {}
        all_buckets = []
        for bucket in init_buckets:
            split_buckets = MB.split(bucket, z)
            for elem in split_buckets:
                all_buckets.append(elem)

        assignments = []
        for i in range(len(all_buckets) - 1, -1, -1):
            prev_bucket = BE.check_bucket(elim_buckets, all_buckets[i])
            c_table = BE.compute_probabilities(all_buckets[i], prev_bucket)
            final, value = BE.eliminate(c_table, all_buckets[i][0])
            elim_buckets.append(final)
            assignments.append((all_buckets[i][0], value))

        for i in assignments:
            if i[0] not in assignment.keys():
                assignment[i[0]] = i[1]
            else:
                assignment[i[0]] = max(assignment[i[0]], i[1])
        return all_buckets, assignment

    @staticmethod
    def split(bucket, z):
        if len(bucket) <= 1:
            return [bucket]
        else:
            remaining = bucket
            mini_buckets = []
            done = False
            while not done:
                mini_bucket = remaining[:z + 1]
                new_remaining = [bucket[0]]
                for node in remaining[z + 1:]:
                    new_remaining.append(node)
                if len(mini_bucket) > 1:
                    mini_buckets.append(mini_bucket)
                remaining = new_remaining
                if len(new_remaining) <= 1:
                    done = True
            return mini_buckets
