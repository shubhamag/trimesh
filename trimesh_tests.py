import trimesh
import unittest
import logging
import numpy as np


TEST_DIR = './models'
TOL_ZERO = 1e-9
log = logging.getLogger('trimesh')
log.addHandler(logging.NullHandler)

class VectorTests(unittest.TestCase):
    def setUp(self):
        self.vector_dim = (100,3)
        self.vectors = np.random.random(self.vector_dim)
        self.vectors = trimesh.unitize(self.vectors)

    def test_unitize(self):
        self.vectors[0:10] = [0,0,0]
        self.vectors = trimesh.unitize(self.vectors)
        self.assertTrue(np.shape(self.vectors) == self.vector_dim)
        
        norms = np.sum(self.vectors ** 2, axis=1) ** 2
        nonzero = norms > TOL_ZERO
        unit_vector = np.abs(norms[nonzero] - 1.0) < TOL_ZERO
        self.assertTrue(np.all(unit_vector))

    def test_group(self):
        tol_angle = np.radians(10)
        tol_dist  = np.tan(tol_angle)

        self.vectors[0:10]  = [0.0, 0.0, 0.0]
        self.vectors[10:20] = [0.0, 0.0, 1.0]
       
        vectors, aligned = trimesh.group_vectors(self.vectors, 
                                                 TOL_ANGLE = tol_angle,
                                                 include_negative = True)
        self.assertTrue(len(vectors) == len(aligned))

        for vector, group in zip(vectors, aligned):
            dists_pos = np.sum((self.vectors[[group]] - vector)**2, axis=1)**.5
            dists_neg = np.sum((self.vectors[[group]] + vector)**2, axis=1)**.5
            dist_ok = np.logical_or((dists_pos < tol_dist), (dists_neg < tol_dist))
            self.assertTrue(np.all(dist_ok))

if __name__ == '__main__':
    unittest.main()