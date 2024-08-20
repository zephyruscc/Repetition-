from collections import defaultdict
import re

def parse_letter_segments(password):
    """从密码中提取出所有字母段"""
    segments = re.findall(r'[a-zA-Z]+', password)
    return segments

def learn_specific_L_segment_probabilities(file_path):
    """从dic-0294.txt中学习具体L段（如sfafa）的概率"""
    specific_L_segment_counts = defaultdict(int)
    total_L_segments = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            L_segments = parse_letter_segments(line)
            for seg in L_segments:
                specific_L_segment_counts[seg] += 1
                total_L_segments += 1

    # 计算每个具体字母段的概率
    specific_L_segment_probabilities = {}
    for seg, count in specific_L_segment_counts.items():
        specific_L_segment_probabilities[seg] = count / total_L_segments

    return specific_L_segment_probabilities

# 从 dic-0294.txt 中学习具体L段的概率
specific_L_segment_probabilities = learn_specific_L_segment_probabilities('dic-0294.txt')

# with open('specific_L_segment_probabilities.txt', 'w', encoding='utf-8') as file:
#     for key, value in specific_L_segment_probabilities.items():
#         file.write(f'{key}: {value}\n')