import math

def main():
    name =  "1 Picnic"
    radius = 6.83
    height = 10.16
    cost = 0.28
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'{name}, {efficiency:.2f} ')

    name =  "1 Tall"
    radius = 7.78
    height = 10.16
    cost = 0.43
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'{name}, {efficiency:.2f} ')

    name =  "2"
    radius = 8.73
    height = 11.59
    cost = 0.45
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "2.5"
    radius = 10.32
    height = 11.91
    cost = 0.61
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "3 Cylinder"
    radius = 10.79
    height = 17.78
    cost = 0.86
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "5"
    radius = 13.02
    height = 14.29
    cost = 0.83
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "6Z"
    radius = 5.40
    height = 8.89
    cost = 0.22
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "8Z short"
    radius = 6.83
    height = 7.62
    cost = 0.26
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "10"
    radius = 15.72
    height = 17.78
    cost = 1.53
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "211"
    radius = 6.83
    height = 12.38
    cost = 0.34
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "300"
    radius = 7.62
    height = 11.27
    cost = 0.38
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')

    name =  "303"
    radius = 8.10
    height = 11.11
    cost = 0.42
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height )
    efficiency = storage_efficiency(volume, surface_area)
    print (f'Name:{name}, storage efficiency:{efficiency:.2f}, cost:{cost} ')




def cylinder_volume(radius, height ):
    volume = math.pi * (radius*radius) * height 
    return volume

def cylinder_surface_area(radius, height ):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def storage_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency
main()