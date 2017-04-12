import time
import glob
import os

# topic = GO_RIDE-booking-log-0

consumer_group = ''
topic = 'a'
date_from = '02-apr-17'

# convert date to epoch timestamp
timestruct = time.strptime(date_from, "%d-%b-%y")
epoch_time = time.mktime(timestruct)

kafka_logs_dir = '/Users/deepakmarathe/workspace/python/'


def getOffset(file):
    return file.split('/')[-1].split('.')[0]


def getIndex(file):
    return file.split('/')[-1].split('.')[0]


# def getOffsetForDate(indexes, e_time):
#     a = 0
#     #sort indexes based on their modified time.
#     # i = indexes.sort(key=os.path.getmtime)
#     #file_modified_time = os.path.getmtime(indexes[0])
#     for f in indexes:
#         offset = getOffset(f)
#         mtime = os.path.getmtime(f)
#         print("file : ", f, " offset : ", offset, " mtime : ", mtime)
#
#     return a
#

def get_min_offset_for_date(kafka_logs_dir, topic, e_time):
    partition_dir = glob.glob(kafka_logs_dir + topic + '-*')
    print("topic : " + topic + ", PARTITIONS : ")
    partition_offset = {}
    for dir in partition_dir:
        offset = getoffset(dir + "/", e_time)
        partition_offset[dir] = offset
        print("dir is ", dir, ", offset is : ", offset)
        # if offset < min:
        #     min = offset
            # indexes = glob.glob(dir + '/*.index')
            # print(indexes)

            # index = getOffsetForDate(indexes, e_time)
            #
            # print("index is : ", index)
            # if index < min:
            #     min = index
    print("topic: ", topic, ", minimum offset: ", min)
    return partition_offset


def getoffset(directory, t_c):
    files = glob.glob(directory + "*.index")
    files.sort(key=os.path.getmtime)
    # print(files)
    # if ( ( files is not None)  and  ( len(files) > 0 )):
    # print("len(files) : " , len(files))

    t = os.path.getmtime(files[0])
    a = []
    for f in files[1:]:
        i = getIndex(f)
        a.append((t, i))
        t = os.path.getmtime(f)

    # print(a)

    prev = a[0]
    for t in a[1:]:
        if t[0] < t_c:
            prev = t

    # print(prev)

    return prev[1]


offset = get_min_offset_for_date(kafka_logs_dir, topic, epoch_time)
print("min is ", offset)



# write(consumer_group + ',' + topic + ',' + min_offset)
