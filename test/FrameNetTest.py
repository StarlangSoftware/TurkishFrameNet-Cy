import unittest

from FrameNet.FrameNet import FrameNet


class FrameNetTest(unittest.TestCase):

    def setUp(self) -> None:
        self.frameNet = FrameNet()

    def test_FrameSize(self):
        self.assertEqual(139, self.frameNet.size())

    def test_LexicalUnitSize(self):
        count = 0
        for i in range(self.frameNet.size()):
            count += self.frameNet.getFrame(i).size()
        self.assertEqual(2561, count)

    def test_FrameElementSize(self):
        count = 0
        for i in range(self.frameNet.size()):
            for j in range(self.frameNet.getFrame(i).size()):
                count += self.frameNet.getFrame(i).getLexicalUnit(j).size()
        self.assertEqual(10476, count)

    def test_DistinctFrameElements(self):
        elements = set()
        for i in range(self.frameNet.size()):
            for j in range(self.frameNet.getFrame(i).size()):
                for element in self.frameNet.getFrame(i).getLexicalUnit(j).getFrameElements():
                    elements.add(element)
        self.assertEqual(203, len(elements))
