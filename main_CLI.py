

import copymovedetection

"""
Main Code
"""

# to detect all images under a directory, use detect_dir
# CopyMoveDetection.detect_dir('../testcase_image/', '../testcase_result/', 32)

# to detect single image, use detect
# CopyMoveDetection.detectblockSize=3('../testcase_image/', '01_barrier_copy.png', '../testcase_result/', 2)




copymovedetection.detect('C:/Users/admn/PycharmProjects/student/testcase/','home.png','C:/Users/admin/PycharmProjects/student/testcaser/', blockSize=32)
