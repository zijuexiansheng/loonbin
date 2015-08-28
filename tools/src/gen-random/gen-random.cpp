#include<iostream>
#include<cstdlib>
#include<ctime>
#include<string>

using namespace std;

void help_msg(const char* fname)
{
    cerr << "Usage: " << fname << " <len> <dict>" << endl;
    cerr << endl;
}

int main(int argc, char* argv[])
{
    if(argc != 3)
    {
        help_msg(argv[0]);
        exit(1);
    }
    int len = atoi(argv[1]);
    string dict = argv[2];

    srand(time(NULL));
    while(len-- > 0)
    {
        int pos = rand() % dict.length();
        cout << dict[pos];
    }
    cout << endl;
    
    return 0;
}
