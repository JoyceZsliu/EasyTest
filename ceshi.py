import unittest
import os

# 假设要测试的文件夹路径
TEST_DIRECTORY = 'C:\ProgramData\Jenkins\.jenkins\workspace\ceshi'

# 文件测试类
class TestFiles(unittest.TestCase):
    
    def test_file_size(self):
        """测试文件大小是否大于0"""
        files = self.get_files_from_directory()
        for file in files:
            with self.subTest(file=file):
                self.assertGreater(os.path.getsize(file), 0, f"{file} 文件大小为0")
    
    def test_file_extension(self):
        """测试文件扩展名是否符合要求"""
        valid_extensions = ['.txt', '.csv', '.json']
        files = self.get_files_from_directory()
        for file in files:
            with self.subTest(file=file):
                self.assertIn(os.path.splitext(file)[1], valid_extensions, f"{file} 文件扩展名不符合要求")

    def get_files_from_directory(self):
        """获取目录中所有文件"""
        return [os.path.join(TEST_DIRECTORY, f) for f in os.listdir(TEST_DIRECTORY) if os.path.isfile(os.path.join(TEST_DIRECTORY, f))]

# 生成测试报告
def generate_test_report():
    # 创建一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFiles)
    
    # 创建一个文本文件保存报告
    with open("test_report.txt", "w") as report_file:
        runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
        runner.run(suite)
        
    print("测试报告已生成: test_report.txt")

if __name__ == '__main__':
    if not os.path.exists(TEST_DIRECTORY):
        print(f"错误：目录 {TEST_DIRECTORY} 不存在！")
    else:
        generate_test_report()
