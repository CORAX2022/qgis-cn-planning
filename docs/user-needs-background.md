# Background: professional course coverage

This is a **background user-needs note**, not a product definition and not a plan for teaching templates. It records the professional course clusters that may use the library, so that resource gaps can be identified without turning the product into a simplified teaching version.

The product is a standards-backed QGIS resource library. Course names are used only to check coverage of professional user needs; they are not written into formal templates, and they do not determine the first template.

## Sources reviewed

- [同济大学 2024 级城乡规划（精英班）培养方案](https://ghc.tongji.edu.cn/__local/3/3F/AD/5C3306FE5138DA3218718A26082_A296798E_DAD7F.pdf)
- [同济大学 2025 级城乡规划学硕士（083300）培养方案](https://caup.tongji.edu.cn/_upload/article/files/39/0d/a4c27b0342138c5b5083621e0d79/e0fc0fc7-e27d-4a7b-bec8-dc475a07e324.pdf)
- [同济大学 2025 级城乡规划硕士（085300）培养方案](https://caup.tongji.edu.cn/_upload/article/files/39/0d/a4c27b0342138c5b5083621e0d79/163f00b9-2f10-4040-bba9-3c40afe89bc6.pdf)
- [清华大学城乡规划专业本科培养方案](https://www.tsinghua.edu.cn/jxjywj/bkzy2022/zxzy/2.pdf)
- [南京大学城市规划专业硕士培养方案](https://arch.nju.edu.cn/njdx/DFS//file/2020/08/27/20200827091624103mydj3s.pdf)

The curricula differ in emphasis, but the course clusters below recur across the reviewed programmes.

## Coverage status

| Status | Meaning |
|---|---|
| Covered | The v0.1.0 domain packs directly address the resource type. |
| Partial | Some resources exist, but a distinct package or sheet type is still missing. |
| Gap | No resource type is defined yet. |

## Matrix

| Course cluster | Typical courses / directions | QGIS resource type | Status | Priority |
|---|---|---|---|---|
| Planning principles and history | 城乡规划原理、城市建设史、城市发展史 | Timeline graphics, historical maps, reference layers, documentation | Partial | P2 |
| Master planning | 总体规划、国土空间总体规划 | Land-use, zoning, three zones and three lines, structure diagrams, facility layout | Covered | P0 |
| Regulatory / site planning | 详细规划设计、控制性详细规划、修建性详细规划 | Parcel boundaries, FAR/height/density, six lines, setbacks, entrances, supporting facilities, site plans | Gap | P0 |
| Urban design | 城市设计、城市形态、公共空间 | Height bands, intensity, street interface, view corridors, public space, street sections, character and colour | Gap | P0 |
| Housing and community | 住区规划、住房与社区建设规划 | Residential land, community life circle, service radius, supporting facilities | Gap | P1 |
| Urban renewal | 城市更新、存量规划 | Renewal units, retain/renovate/demolish, inefficient land, vacant land, micro-renewal | Gap | P1 |
| Transport | 城市道路与交通、城市与区域交通规划 | Road hierarchy, cross-sections, bus/rail, slow traffic, parking, terminals | Gap | P0 |
| Municipal infrastructure | 城市工程系统、市政基础设施 | Water, drainage, power, gas, heating, telecom, sanitation, utility corridors | Gap | P0 |
| Disaster prevention | 城市防灾、公共安全 | Flood, fire, shelters, geological hazards, lifelines | Gap | P1 |
| Ecology and environment | 城市生态与环境规划、绿地系统、海绵城市 | Ecological sensitivity, corridors, green system, sponge city, carbon | Gap | P0 |
| Regional planning | 区域规划、区域研究与规划、城镇体系 | Settlement hierarchy, functions, influence areas, shared facilities, metropolitan areas | Partial | P0 |
| Urban geography, economics, sociology | 城市地理、城市经济、城市社会学 | Population density/structure, jobs-housing, social space, land value | Gap | P1 |
| GIS, remote sensing, spatial analysis | 地理信息系统、空间信息技术、城市模型 | Accessibility, heatmaps, suitability, spatiotemporal behaviour, simulation | Gap | P1 |
| Landscape architecture | 风景园林、景观风貌、绿地系统 | Park systems, greenways, planting, landscape structure | Gap | P1 |
| Architecture and site | 建筑设计、场地规划与设计 | Building fabric, height, sunlight, wind, site grading | Gap | P2 |
| Planning administration and law | 城乡规划管理与法规、规划实施 | Control units, permits, one-map system, boundary control | Gap | P1 |
| Healthy cities | 健康城市、公共卫生 | Health facilities, walkability, blue-green space | Gap | P2 |
| Underground space | 地下空间规划 | Underground layers, connectivity, entrances | Gap | P2 |
| Tourism and industry | 旅游规划、产业规划 | Tourism resources, routes, service facilities, industry zones | Partial | P1 |
| Heritage conservation | 城乡发展历史与遗产保护规划、城市文化与历史保护 | Historic towns/villages, protected areas, buffer zones, historic buildings, character zones, heritage routes | Covered | P0 |
| Village and town planning | 乡村规划设计、乡村规划实务、村镇规划 | Village classification, settlement system, land layout, facilities, roads, industry | Covered | P0 |

## Interpretation

- **Covered** does not mean complete. The domain pack may still lack sheet variants, legends, or local profiles.
- **Partial** means the topic appears inside another pack but has no dedicated symbol set, sheet type, or documentation.
- **Gap** means a contributor would currently have to build the resource from scratch.

## Prioritisation logic

P0 resources are those needed by the core studio sequence and by the first public release: master planning, regulatory/site planning, urban design, transport, municipal infrastructure, ecology, regional planning, heritage, and village/town planning.

P1 resources extend the library into specialist practice: housing, renewal, disaster prevention, geography/economics/sociology, GIS analysis, landscape, planning administration, and tourism/industry.

P2 resources are valuable but can be deferred: planning history, architecture/site, healthy cities, and underground space.

Priorities are recommendations for release planning, not a judgement about the importance of a course.

## What a course does not imply

- A course title does not automatically require a new QGIS template. Some courses need documentation, sample data, or analysis workflows rather than symbols.
- A single resource may serve several courses; for example, a parcel style can support regulatory planning, urban design, and renewal.
- Local profiles may override national conventions; the library must not flatten them into one style.

## Next step

For each Gap or Partial row, the v0.1.0 milestone should decide whether to:

1. add a resource pack,
2. document a future pack,
3. explicitly mark it out of scope for v0.1.0.

The decision should be recorded in the milestone issue rather than left implicit in this table.
