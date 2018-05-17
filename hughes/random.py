#Created by D.J.Hughes May 2018

import numpy, matplotlib.pylab

class RanDist(object):
    
    """An array of random numbers from specificed distribution
    
    Args:
        nrand (int): number of random numbers to be generated
        dist_type (str): distribution type from which to generate nrand random numbers = 'normal', 'poisson' or 'binomial'
        **kwargs (optional): extra keyword arguments for the numpy.random.dist_type functions, these are (= defaults):
            - dist_type = 'normal' **kwargs: loc = 0.0 (centre / mean), scale = 1.0 (standard deviation)
            - dist_type = 'binomial' **kwargs: n (no. of trials (>=0)), p (probability of success (0<=p<=1)) (no defaults)
            - dist_type = 'poisson' **hwargs: lam = 1.0 (lambda)
        
    Attributes:
        (leading '_' on attribute names mean private / should not be changed once created in object)
        _nrand (int): number of random numbers generated
        _dist_type (str): distribution type from which nrand random numbers have been generated = 'normal', 'poisson' or 'binomial'
        _kwargs (dict): dictionary of kwargs for numpy.random.dist_type 
        _rand_nums: array of nrand random numbers from dist_type distribution
    """
    
    def __init__(self, nrand = 1, dist_type = 'normal', **kwargs):
        
        self._nrand = nrand
        self._dist_type = dist_type
        self._kwargs = kwargs
        
        if self._dist_type == 'normal':
            self._rand_nums = numpy.random.normal(size = self._nrand, **kwargs)
            
        elif self._dist_type == 'poisson':
            self._rand_nums = numpy.random.poisson(size = self._nrand, **kwargs)
            
        elif self._dist_type == 'binomial':
            self._rand_nums = numpy.random.binomial(size = self._nrand, **kwargs)
        
        elif self._dist_type != ('normal' or 'poisson' or 'binomial'):
            
            raise Exception("dist_type option unrecognised")
            
    def __repr__(self):
        
        """return call command of object self and list of generated random numbers"""
        
        return "<RanDist(nrand = %s, dist_type = '%s', **kwargs = %s)> \n %s" % (self._nrand, self._dist_type, self._kwargs, 
                                                                                           self._rand_nums)
    
    def summary(self):
        
        """return summary of key attributes and statistical quantities of self._rand_nums"""
        
        print("Summary for: <class RanDist(nrand = %s, dist_type = '%s', **kwargs = %s)>" % (self._nrand, self._dist_type, self._kwargs))
        print("(_rand_nums = object_name._rand_nums)")
        summary_table = {'dist_type': self._dist_type,
						 'nrand': self._nrand,
                         'min(_rand_nums)': numpy.min(self._rand_nums),
                         'max(_rand_nums)': numpy.max(self._rand_nums),
                         'mean(_rand_nums)': numpy.mean(self._rand_nums), 
                         'median(_rand_nums)': numpy.median(self._rand_nums),
                         'stdev(_rand_nums)': numpy.std(self._rand_nums)}
        for attr, val in summary_table.items(): #formatted output of summary_table entries
            print('{0:15} : {1:15}'.format(attr, str(val)))
            
    def hist(self):
        
        """basic histogramming plot of self._rand_nums, specified unitary bin widths for discrete distributions 
        (poisson and binomial), otherwise left to matplotlib.pylab.hist() autobinning"""
        
        if self._dist_type == ('poisson'):
            matplotlib.pylab.hist(self._rand_nums, bins = int(numpy.max(self._rand_nums) - numpy.min(self._rand_nums)))
        if self._dist_type == ('binomial'):
            matplotlib.pylab.hist(self._rand_nums, bins = int(numpy.max(self._rand_nums) - numpy.min(self._rand_nums)))
        if self._dist_type == ('normal'):
            matplotlib.pylab.hist(self._rand_nums)
        
        matplotlib.pylab.xlabel('sample value')
        matplotlib.pylab.ylabel('frequency')
        matplotlib.pylab.title("<class RanDist(nrand = %s, dist_type = '%s', **kwargs = %s)>" % (self._nrand, self._dist_type, self._kwargs))
        matplotlib.pylab.show()
