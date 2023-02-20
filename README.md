# mywork

My Work area

Input:
```python
for i in list:
    print(i)
```
Output:
```
The total in Euros and Cents is: €23.54
```

Mermaid:
https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/


```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

```mermaid
flowchart TD;
    A[Enter a number] --> B{number == 1?};
    B -- Yes --> G[End];
    B -- No --> C{Even?};
    C -- Yes --> D[/2];
    C -- No --> E[*3-1];
    D --> B;
    E --> B;
```