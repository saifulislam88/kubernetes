

### Pod scheduling কীভাবে হয়?

#### 📘 এই লেখায় যা থাকছে:
- Pod কী এবং কেন ব্যবহৃত হয়
- `db.yml` ফাইল ব্যাখ্যা
- Kubernetes-এ Pod Scheduling-এর প্রধান component গুলো
- Step-by-step scheduling প্রসেস

#### 🧱 Kubernetes Pod & db.yml Explained

Kubernetes-এ container সরাসরি চালানো যায় না। আমরা container-কে **Pod** এর ভেতরে চালাই। Pod হলো Kubernetes-এর সবচেয়ে ছোট deployable unit।

নিচে একটি সাধারণ Pod definition (`db.yml`) দেওয়া হলো:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db
  labels:
    type: db
    vendor: MongoLabs
spec:
  containers:
  - name: db
    image: mongo:3.3
    command: ["mongod"]
    args: ["--rest", "--httpinterface"]
```

##### 📄 `db.yml` ব্যাখ্যা

| লাইন | ব্যাখ্যা |
|------|----------|
| 1–2  | `apiVersion` ও `kind`—এগুলো Kubernetes-কে জানায় আমরা কোন ধরনের resource তৈরি করতে চাই (এখানে Pod) এবং কোন API version ব্যবহার করব।। |
| 3–7  | `metadata` অংশে Pod-এর নাম এবং কিছু label রয়েছে। এগুলো পরবর্তীতে selectors বা controllers-এ ব্যবহারযোগ্য। |
| 8    | `spec`-এ container সংক্রান্ত তথ্য থাকে। |
| 9–11 | container-এর নাম `db`, image হিসেবে `mongo:3.3` ব্যবহৃত হয়েছে। |
| 12   | container চালু হলে `mongod` কমান্ড চলবে। |
| 13   | দুটি argument: `--rest`, `--httpinterface` চালু করা হয়েছে। |

---

#### ⚙️ Pod Scheduling-এ জড়িত প্রধান ৩টি Component

##### 1️⃣ API Server
- এটি পুরো cluster-এর মস্তিষ্ক।
- সব communication, authentication, এবং object management এখান দিয়ে হয়।

##### 2️⃣ Scheduler
- যেসব Pod এখনো কোনো node-এ assign হয়নি (unassigned), তাদের detect করে।
- উপযুক্ত node খুঁজে নিয়ে, সেই node-এ Pod assign করে দেয়।

##### 3️⃣ Kubelet
- প্রতিটি worker node-এ চালিত হয়।
- Scheduler যেই node-এ Pod assign করে, সেই node-এর Kubelet container তৈরি করে এবং চালায়।

---

#### 🔁 Step-by-Step Pod Scheduling Flow

1. **Pod Creation:**
   - `kubectl create -f db.yml` দিলে client API server-এ Pod তৈরির request পাঠায়।
2. **Detection by Scheduler:**
   - API server দেখতে পায় একটি unassigned Pod এসেছে।
3. **Node Assignment:**
   - Scheduler resource-based decision নিয়ে একটি node নির্বাচন করে Pod assign করে।
4. **Kubelet Trigger:**
   - Assigned node-এর Kubelet API server থেকে জানতে পারে তার node-এ নতুন Pod রান হবে।
5. **Container Launch:**
   - Kubelet, container runtime (যেমন Docker) কে Pod অনুযায়ী container চালাতে বলে।
6. **Status Reporting:**
   - Pod সফলভাবে চালু হলে, Kubelet API server-এ জানিয়ে দেয়।

---

