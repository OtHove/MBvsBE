from Network import Network
from Node import Node
from statistics import mean


class BE:

    @staticmethod
    def solve_be(network, ordering):
        all_buckets = BE.bucket(network, ordering)
        elim_buckets = []
        assignment = {}
        for i in range(len(all_buckets) - 1, -1, -1):
            prev_bucket = BE.check_bucket(elim_buckets, all_buckets[i])
            c_table = BE.compute_probabilities(all_buckets[i], prev_bucket)
            final, value = BE.eliminate(c_table, ordering[i])
            elim_buckets.append(final)
            assignment[ordering[i]] = value
        return all_buckets, assignment

    @staticmethod
    def handled(node, c_node, ordering):
        index = 0
        c_index = 0
        for i in range(0, len(ordering)):
            if ordering[i] == node:
                index = i
            else:
                if ordering[i] == c_node:
                    c_index = i

        if index < c_index:
            return True
        else:
            return False

    @staticmethod
    def check_bucket(elim_buckets, bucket):
        x = len(elim_buckets)
        if x < 1:
            return []
        while x >= 0:
            x = x-1
            if x <= 0:
                return []
            if elim_buckets[x]:
                for c_node in elim_buckets[x][0]:
                    for t_node in bucket:
                        if c_node == t_node:
                            return elim_buckets[x]

    @staticmethod
    def compute_probabilities(bucket, prev_bucket):
        table = BE.get_table(bucket)
        if not prev_bucket:
            return table
        if len(prev_bucket) > 0:
            prev_nodes = list(prev_bucket[0].keys())
            for x in prev_nodes:
                if not isinstance(x, Node):
                    prev_nodes.remove(x)
        else:
            prev_nodes = []
        for node in prev_nodes:
            if node not in bucket:
                length = len(table)
                for index in range(0, len(table)):
                    table[index][node] = 0
                    table.append(table[index])
                    table[length + index][node] = 1

        for i in range(0, len(prev_bucket)):
            common_nodes = list()
            for node in prev_nodes:
                if node in bucket:
                    common_nodes.append(node)
            for row in range(0, len(table)):
                matches = True
                for x in common_nodes:
                    if not prev_bucket[i][x] == table[row][x]:
                        matches = False
                if matches:
                    table[row]["label"] = table[row]["label"] * prev_bucket[i]["label"]
        return table

    @staticmethod
    def eliminate(c_table, node):
        if node not in c_table[0].keys():
            labels = []
            for row in c_table:
                labels.append(row["label"])
            return [], mean(labels)
        node_true = 0
        node_total = 0
        for row in c_table:
            if row[node] == 1:
                node_true = node_true + row["label"]
            node_total = node_total + row["label"]
        del c_table[0][node]
        if node_total == 0:
            prob_true = 0
        else:
            prob_true = node_true / node_total
        return c_table, prob_true

    @staticmethod
    def get_table(bucket):
        table = [{}]
        for node in bucket:
            length = len(table)
            for i in range(0, length):
                if length == 0:
                    table.append({node: 0})
                    table.append({node: 1})
                else:
                    table[i][node] = 0
                    row = {}
                    for key in table[i]:
                        row[key] = table[i][key]
                    table.append(row)
                    table[length + i][node] = 1
        result = []
        for nodes_index in range(0, len(table)):
            prob = 1
            keys = list(table[nodes_index].keys())
            for x in keys:
                if not isinstance(x, Node):
                    keys.remove(x)
            for key in keys:
                sh_parents = []
                for parent in key.parents:
                    if parent in keys:
                        sh_parents.append(parent)
                combination = {}
                for parent in sh_parents:
                    combination[parent] = table[nodes_index][parent]
                c_prob = 0
                a_prob = 0
                for row in key.label:
                    corresponds = True
                    for node in list(combination.keys()):
                        if not combination[node] == row[node]:
                            corresponds = False
                    if corresponds:
                        c_prob = c_prob + row.get("label", 0.5)
                    a_prob = a_prob + row.get("label", 0.5)
                prob = float(prob) * (c_prob / a_prob)
            table[nodes_index]["label"] = prob
            result.append(table[nodes_index])
        return result

    @staticmethod
    def bucket(network, ordering):
        buckets = list()
        for c_node in ordering:
            bucket = list()
            bucket.append(c_node)
            for p_node in c_node.parents:
                if not BE.handled(p_node, c_node, ordering):
                    bucket.append(p_node)
            for n_node in network.get_network():
                for p_node in n_node.parents:
                    if p_node == c_node and not BE.handled(n_node, c_node, ordering):
                        bucket.append(n_node)
            buckets.append(bucket)
        return buckets