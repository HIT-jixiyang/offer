# n_2=int(input())
# P=[]
# for i in range(n_2):
#     [x,y]=list(map(int,input().split(' ')))
#     P.append((int(x),int(y)))
# 
#include<iostream>
using namespace std;

const int N = 14;

struct point
{
    int x;
    int y;
};

bool flag[N];

void dfs(struct point P[],struct point v[],int index,int n,int & ans,int & count);

int main()
{
    struct point P[N];
    struct point v[N];
    int i;
    int n;
    int ans = 0,count = 0;
    cin >> n;
    for(i = 0 ; i < n ; i++ )
        flag[i] = false;
    for(i = 0 ; i < n ;i++ )
        cin >> P[i].x >> P[i].y;
    dfs(P,v,0,n,ans,count);
    cout << ans << endl;
    return 0;
}

void dfs(struct point P[],struct point v[],int index,int n,int & ans,int & count)
{
    int i,j,temp = 0;
    while(flag[index])
        index++;
    if(index >= n)
    {
        for(i = 0 ; i < count ; i++ )
            for(j = i + 1 ; j < count ; j++ )
                if(v[i].x * v[j].y == v[i].y * v[j].x)
                    temp++;
        ans = max(ans,temp);
        return;
    }
    flag[index] = 1;
    for(i = 0 ; i < n ; i++ )
    {
        if(!flag[i])
        {
            flag[i] = 1;
            v[count].x = P[index].x - P[i].x;
            v[count].y = P[index].y - P[i].y;
            count++;
            dfs(P,v,index + 1,n,ans,count);
            count--;
            flag[i] = false;
        }
    }
    flag[index] = false;
    return ;
}
————————————————
版权声明：本文为CSDN博主「GOoAT」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43960546/java/article/details/98550941