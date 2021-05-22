#include<bits/stdc++.h>
#include<iostream>
using namespace std;

void printGraph(vector<vector<pair<int,int>>>g)
{
    int ii=1;
    for(auto i :g)
    {
        cout<<ii<<" : ";
        ++ii;
        for(auto j:i)
        {
            cout<<j.first<<"->"<<j.second<<" ";
        }
        cout<<endl;
    }
}

void bfs(vector<vector<pair<int,int>>>G){
    vector<bool>visited(G.size()+1,false);
    
}

int main()
{
    int n,m;
    cin>>n>>m;
    vector<vector<pair<int,int>>>graph(n+1);

    while (m--)
    {
        int u,v,w;
        cin>>u>>v>>w;
        graph[u].push_back({v,w});//vertex,weight
    }

    printGraph(graph);
    return 0;
}
