import numpy as np

def triplet_generator(batch_size=4):
    ''' Dummy triplet generator for API usage demo only.

    Will be replaced by a version that uses real image data later.

    :return: a batch of (anchor, positive, negative) triplets
    '''
    while True:
        a_batch = np.random.rand(batch_size, 96, 96, 3)
        p_batch = np.random.rand(batch_size, 96, 96, 3)
        n_batch = np.random.rand(batch_size, 96, 96, 3)
        # The target can be dummy, e.g., zeros. It's not used in the triplet loss directly.
        dummy_target = np.zeros((batch_size, 1))
        yield [a_batch, p_batch, n_batch], dummy_target