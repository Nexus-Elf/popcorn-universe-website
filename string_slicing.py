import math
def main():
    d = {'Mark': 100.0, 'Peter': 50.0, 'John': 25.0}
    sorted_items = sorted(d.items(), key=lambda e: e[1], reverse=True)
    print('\n'.join('{} pays {}'.format(k, int(v)) for k, v in sorted_items))
if __name__ == "__main__":
    pass
main()