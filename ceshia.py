import unittest
import os
import importlib.util


class TestFiles(unittest.TestCase):

    def test_python_files(self):
        """测试当前目录及子目录中的所有 Python 文件是否可以被成功导入并执行"""
        files = self.get_files_from_directory()
        for file in files:
            with self.subTest(file=file):
                try:
                    # 动态加载模块并执行
                    module_name = os.path.splitext(os.path.basename(file))[0]
                    spec = importlib.util.spec_from_file_location(module_name, file)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    self.assertTrue(True, f"{file} 执行成功")
                except Exception as e:
                    self.fail(f"{file} 执行失败: {str(e)}")

    def get_files_from_directory(self):
        """获取当前目录及其子目录中的所有 Python 文件"""
        # 当前目录及所有子目录
        current_directory = os.getcwd()
        python_files = []
        for root, dirs, files in os.walk(current_directory):
            for file in files:
                if file.endswith('.py') and file != os.path.basename(__file__):  # 排除当前测试脚本
                    python_files.append(os.path.join(root, file))
        return python_files


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
    generate_test_report()
