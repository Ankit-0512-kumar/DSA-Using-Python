import java.util.*;

public class TushFormatNjTOC {
    
    static class Node {
        String name;
        Node parent;
        List<Node> children;
        boolean locked;
        int lockedBy;
        int locDescCnt; // locked descendant count

        Node(String name) {
            this.name = name;
            this.children = new ArrayList<>();
            this.locked = false;
            this.lockedBy = 0;
            this.locDescCnt = 0;
        }
    }

    static Map<String, Node> nodeMap = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int m = sc.nextInt();
        int Q = sc.nextInt();
        sc.nextLine(); // Consume leftover newline

        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            String name = sc.nextLine().trim();
            nodes[i] = new Node(name);
            nodeMap.put(name, nodes[i]);
        }

        for (int i = 0; i < N; i++) {
            Node cur = nodes[i];
            for (int j = 1; j <= m; j++) {
                int childIndex = m * i + j;
                if (childIndex < N) {
                    Node child = nodes[childIndex];
                    child.parent = cur;
                    cur.children.add(child);
                } else {
                    break;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            int op = sc.nextInt();
            String nodeName = sc.next();
            int uid = sc.nextInt();

            boolean res = false;
            Node node = nodeMap.get(nodeName);

            switch (op) {
                case 1:
                    res = lock(node, uid);
                    break;
                case 2:
                    res = unlock(node, uid);
                    break;
                case 3:
                    res = upgradeLock(node, uid);
                    break;
            }

            sb.append(res ? "true" : "false").append("\n");
        }

        System.out.print(sb);
    }

    private static boolean lock(Node node, int uid) {
        if (node.locked) return false;
        Node parent = node.parent;
        while (parent != null) {
            if (parent.locked) return false;
            parent = parent.parent;
        }
        if (node.locDescCnt > 0) return false;

        node.locked = true;
        node.lockedBy = uid;
        parent = node.parent;
        while (parent != null) {
            parent.locDescCnt++;
            parent = parent.parent;
        }
        return true;
    }

    private static boolean unlock(Node node, int uid) {
        if (!node.locked || node.lockedBy != uid) return false;

        node.locked = false;
        node.lockedBy = 0;
        Node parent = node.parent;
        while (parent != null) {
            parent.locDescCnt--;
            parent = parent.parent;
        }
        return true;
    }

    private static boolean upgradeLock(Node node, int uid) {
        if (node.locked || node.locDescCnt == 0) return false;

        List<Node> lockedNodes = new ArrayList<>();
        if (!dfsCheckAndCollect(node, uid, lockedNodes)) return false;

        for (Node lockedNode : lockedNodes) {
            unlock(lockedNode, uid);
        }

        return lock(node, uid);
    }

    private static boolean dfsCheckAndCollect(Node node, int uid, List<Node> lockedNodes) {
        for (Node child : node.children) {
            if (child.locked || child.locDescCnt > 0) {
                if (child.locked) {
                    if (child.lockedBy != uid) return false;
                    lockedNodes.add(child);
                }
                if (!dfsCheckAndCollect(child, uid, lockedNodes)) return false;
            }
        }
        return true;
    }
}
