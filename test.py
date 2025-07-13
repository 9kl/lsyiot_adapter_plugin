# -*- coding: utf-8 -*-

from filters import __filters__
from pdmparse.api import PdmParse
from pdmparse.parsers import read


def gen_model():
    def table_filter_func(table):
        return len([diagram for diagram in table.diagrams if diagram.name == '服务系统']) > 0

    def rename(table):
        f_name = '%s.py' % (table.code.lower())
        print(f_name)
        return f_name

    api = PdmParse(r'C:\Users\china\OneDrive\Dev\pdm\lnwork_open.pdm', 'templates', __filters__)
    api.gen_template_file('output', 'flask_api.jinja2',
                          table_filter_func, rename, **{'app_name': 'app_name', 'package_name': 'package_name'})


def print_read():
    """测试read方法读取的XML解析到FnTable中的值，并输出到屏幕
    """
    tables = read(r'C:\Users\china\OneDrive\Dev\pdm\lnwork_open.pdm')
    for t in tables:
        print(f'\n##################################{t.name}##################################')
        print(t)

        print('columns:')
        for column in t.columns:
            print(column)

        print('parentrefs:')
        for ref in t.parent_refs:
            print(ref)

        print('childrefs:')
        for ref in t.child_refs:
            print(ref)

        print('diagrams:')
        for diagram in t.diagrams:
            print(diagram)


def main():
    print_read()
    # gen_model()


if __name__ == "__main__":
    main()
