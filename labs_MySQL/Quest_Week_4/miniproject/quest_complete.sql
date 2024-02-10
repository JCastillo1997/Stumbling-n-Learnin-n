use mydb;
select count(id_alumnos) as nº_alumnos ,alcohol_diario as grado_alcoholismo ,escuela, tiempo_libre from alumnos
left join ocio using(ocio_id)
left join colegios on colegios.colegios_id= alumnos.colegios_id
where alcohol_diario >= 3
group by escuela, alcohol_diario, tiempo_libre order by tiempo_libre desc;

-- en esta query hemos mirado si el tiempo libre afecta al consumo de alcohol diario entre los alumnos de los colegios, no es concluyente.

select count(id_alumnos) as nº_alumnos, estado, (alcohol_diario + alcohol_finde)as Grado_alcohol from padres
left join alumnos using(padres_id)
left join ocio on ocio.ocio_id = alumnos.ocio_id
group by estado, Grado_alcohol order by Grado_alcohol desc;

-- en esta hipotesis hemos estudiado el grado de alcolismo en funcion de si cohabitan los padres o no , es muy significativo el estar separado son mas alcoholicos

select count(id_alumnos) as nº_alumnos ,(alcohol_diario+alcohol_finde) as grado_alcoholismo ,pareja from alumnos
join ocio using(ocio_id)
where pareja = "no" and alcohol_diario+alcohol_finde > 5
group by pareja, grado_alcoholismo;

 -- en esta hipotesis hemos estudiado el grado de alcolismo de las personas con pareja, beben menos que los alumnos que no tienen pareja

select count(id_alumnos) as nº_alumnos, (educacion_m+eduacion_p) as educacion_padres, (alcohol_diario + alcohol_finde)as Grado_alcohol from padres
left join alumnos using(padres_id)
left join ocio on ocio.ocio_id = alumnos.ocio_id
where alcohol_diario + alcohol_finde > 5
group by educacion_padres, Grado_alcohol order by educacion_padres desc;

-- en este estudio no hay relevancia de que la eduacion de los padres afecte al nivel de alcolismo de los alumnos