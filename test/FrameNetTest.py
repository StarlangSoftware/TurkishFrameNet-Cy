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
            count += self.frameNet.getFrame(i).lexicalUnitSize()
        self.assertEqual(2561, count)

    def test_FrameElementSize(self):
        count = 0
        for i in range(self.frameNet.size()):
            count += self.frameNet.getFrame(i).frameElementSize()
        self.assertEqual(1665, count)

    def test_DistinctFrameElements(self):
        elements = set()
        for i in range(self.frameNet.size()):
            for j in range(self.frameNet.getFrame(i).frameElementSize()):
                elements.add(self.frameNet.getFrame(i).getFrameElement(j))
        self.assertEqual(289, len(elements))
