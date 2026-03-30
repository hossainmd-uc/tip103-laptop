def filter_sustainable_brands(brands, criterion):
    l = []
    for dict in brands:
        n = dict['name']
        c = dict['criteria']
        if criterion in c:
            l.append(n)
    return l

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))

def count_material_usage(brands):
    d = {}
    for dict in brands:
        # n = dict['name']
        m = dict['materials']
        
        for mat in m:
            if mat not in d:
                d[mat] = 1
            else:
                d[mat] += 1
    return d
        
        
    
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))

def find_trending_materials(brands):
    s = set()
    f = []
    for dict in brands:
        n = dict['name']
        m = dict['materials']
        for material in m:
            if material in s:
             f.append(material)
            else:
                s.add(material)
    return f
    

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(find_trending_materials(brands))
# print(find_trending_materials(brands_2))
# print(find_trending_materials(brands_3))

def find_best_fabric_pair(fabrics, budget):
    # Basically I want to see which combination yields highest amount without
        #exceeding the target
    #I would need to do a one pass through the data, then if i use a 
    # diff data struc to minimize the difference
    
    
    fabrics = sorted(fabrics, key=lambda entry: entry[1])
    
    p1 = 0
    p2 = len(fabrics)-1
    
    last = None
    
    while p1 < p2:
        
        p1c = fabrics[p1][1]
        p2c = fabrics[p2][1]
        
        total = p1c + p2c
        
        if total <= budget:
            if total == budget:
                return (fabrics[p1][0], fabrics[p2][0])
            if last:
                if total > last[2]: 
                    last = (fabrics[p1], fabrics[p2], p1c + p2c)
            else:
                last = (fabrics[p1], fabrics[p2], p1c + p2c)
            p1 += 1
        else:
            p2 -= 1

    if last:
        return (last[0][0], last[1][0])
    else:
        return None
            
    print(fabrics)


fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

# print(find_best_fabric_pair(fabrics, 45))
# print(find_best_fabric_pair(fabrics_2, 70))
# print(find_best_fabric_pair(fabrics_3, 60))
import heapq
def organize_fabrics(fabrics):
    
    fabrics = [(-x[1], x[0]) for x in fabrics]
    heapq.heapify(fabrics)
    
    final = []
    while fabrics:
        final.append(heapq.heappop(fabrics)[1])
        
    return final


fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

# print(organize_fabrics(fabrics))
# print(organize_fabrics(fabrics_2))
# print(organize_fabrics(fabrics_3))
#Space: O(n)
#Time: O(n*logn) bc we are popping which takes logn complexity to reorganize

def process_supplies(supplies):
    
    supplies = [(-x[1], x[0]) for x in supplies]
    heapq.heapify(supplies)
    
    f = []
    while supplies:
        f.append(heapq.heappop(supplies)[1])
    
    return f

supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

print(process_supplies(supplies))
print(process_supplies(supplies_2))
print(process_supplies(supplies_3))