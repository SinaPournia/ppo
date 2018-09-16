STATE_SHAPE = [84, 84]
STATE_WINDOW = 4
CONVS = [(32, 8, 4), (64, 4, 2), (64, 3, 1)]
FCS = [512]
PADDING = 'VALID'
LSTM_UNIT = 512
FINAL_STEP = 80e6
RANDOM_SEED = 1
ACTORS = 8

LSTM = False
VALUE_FACTOR = 1.0
ENTROPY_FACTOR = 0.01
EPSILON = 0.1
LR = 2.5e-4
LR_DECAY = 'linear'
GRAD_CLIP = 0.5
TIME_HORIZON = 128
BATCH_SIZE = 32
GAMMA = 0.99
LAM = 0.95
EPOCH = 3
