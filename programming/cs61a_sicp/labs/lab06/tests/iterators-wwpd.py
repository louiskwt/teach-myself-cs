test = {
  'name': 'Iterators',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Enter StopIteration if StopIteration exception occurs, Error for other errors
          >>> # Enter Iterator if the output is an iterator object.
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s) 
          Error
          >>> next(t)
          1
          >>> next(t)
          2
          >>> iter(s)
          Iterator
          >>> next(iter(s))
          1
          >>> next(iter(s))
          1
          >>> next(t)
          3
          >>> next(t)
          4
          >>> next(t)
          StopIteration
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          0
          >>> [x + 1 for x in r]
          [1, 2, 3, 4, 5, 6]
          >>> [x + 1 for x in r_iter]
          [2, 3, 4, 5, 6]
          >>> next(r_iter)
          StopIteration
          >>> list(range(-2, 4))   # Converts an iterable into a list
          [-2, -1, 0, 1, 2, 3]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          10
          >>> next(map_iter)
          11
          >>> list(map_iter)
          [12, 13, 14]
          >>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
          ...     print(e)
          1000
          1002
          1004
          1006
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          [5, 7, 9]
          >>> for e in zip([10, 9, 8], range(3)):
          ...   print(tuple(map(lambda x: x + 2, e)))
          (12, 2)
          (11, 3)
          (10, 4)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}
