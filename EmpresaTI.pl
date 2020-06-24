%declaracion de librerias para la interfaz

:-use_module(library(pce)).
:-use_module(library(pce_style_item)).

% metodo principal para iniciar la interfaz grafica, declaracion de
% botones, labels, y la pocicion en pantalla.
inicio:-
	new(Menu, dialog('Proyect SDM version Alienigena 1.3', size(1000,800))),
	new(L,label(nombre,'Empresa de TI')),
	new(A,label(nombre,'hecho por Mauricio Valencia Valencia 16590524')),
	new(@texto,label(nombre,'responde un breve cuestionario para conocer tu perfil')),
	new(@respl,label(nombre,'')),
	new(Salir,button('SALIR',and(message(Menu, destroy),message(Menu,free)))),
	new(@boton,button('realizar test',message(@prolog,botones))),


	send(Menu,append(L)),new(@btncarrera,button('Diagnostico?')),
	send(Menu,display,L,point(125,20)),
	send(Menu,display,A,point(80,360)),
	send(Menu,display,@boton,point(100,150)),
	send(Menu,display,@texto,point(20,100)),
	send(Menu,display,Salir,point(20,400)),
	send(Menu,display,@respl,point(20,130)),
	send(Menu,open_centered).

%Resultados de los trabajos

fallas('ASISTENTE DE DBA'):-dba,!.

fallas('DESARROLLADOR BACKEND JUNIOR'):-dbj,!.

fallas('DESARROLLADOR FRONTEND JUNIOR'):-dfj,!.

fallas('SYSADMIN'):-adm,!.

fallas('sin resultados, usted no dio la informacion necesaria o suficiente
ERROR p560c4!').

% preguntas para dirigir a la enfermedad adecuada con su respectivo
% identificador de enfermedad

dba:- sdba,
	pregunta('¿Garantizar la alta disponibilidad de la base de datos?'),
	pregunta('¿Diseña la distribución de los datos y las soluciones de almacenamiento?'),
	pregunta('¿Implementa planes de mantenimiento de la base de datos?');
	pregunta('¿Desarrollar tareas de tuning de base de datos?');
	pregunta('¿Desarrollas auditorias de usuarios (roles, perfiles y privilegios)?');
    pregunta('¿Administra cambios y actualizaciones de una base de datos?').

dbj:- sdbj,
    pregunta('¿Maneja de al menos un Framework? '),
	pregunta('¿Tiene conocimientos básicos de configuraciones de servidores web?'),
	pregunta('¿Cuenta con capacidad de abstracción lógica?');
	pregunta('¿Maneja de al menos un CMS?').

dfj:- sdfj,
	pregunta('¿Cuenta con habilidades en HTML5 y CSS3?'),
    pregunta('¿Tiene conocimientos en Javascript y en especial jQuery?');
	pregunta('¿Domina los estándares internacionales para la construcción de HTML?');
	pregunta('¿Sabe manipular al menos un CMS?').

adm:- sadm,
	pregunta('¡Sabe instalar nuevos servidores?'),
	pregunta('¿Sabe configur del hardware de los equipos?');
	pregunta('¿Sabe hacer respaldos?');
	pregunta('¿Sabe instalar y actualizar el software? ');
    pregunta('¿Sabe gestionar cuentas de usuarios?').

%identificador de falla que dirige a las preguntas correspondientes

sdba:-pregunta('¿Sabe instalar, configurar y gestionar bases de datos?'),!.
sdbj:-pregunta('¿Conocimientos y capacidad de estudio de lenguajes de programacion?'),!.
sdfj:-pregunta('¿Tiene conocimientos de diseño y manejar los elementos visuales de un sitio web?'),!.
sadm:-pregunta('¿Sabe monitorear el rendimiento del sistema?'),!.

% proceso del diagnostico basado en preguntas de si y no, cuando el
% usuario dice si, se pasa a la siguiente pregunta del mismo ramo, si
% dice que no se pasa a la pregunta del siguiente ramo


:-dynamic si/1,no/1.
preguntar(Problema):- new(Di,dialog('Diagnostico medico')),
     new(L2,label(texto,'Responde las siguientes preguntas')),
     new(La,label(prob,Problema)),
     new(B1,button(si,and(message(Di,return,si)))),
     new(B2,button(no,and(message(Di,return,no)))),

         send(Di,append(L2)),
	 send(Di,append(La)),
	 send(Di,append(B1)),
	 send(Di,append(B2)),

	 send(Di,default_button,si),
	 send(Di,open_centered),get(Di,confirm,Answer),
	 write(Answer),send(Di,destroy),
	 ((Answer==si)->assert(si(Problema));
	 assert(no(Problema)),fail).

% cada vez que se conteste una pregunta la pantalla se limpia para
% volver a preguntar

pregunta(S):-(si(S)->true; (no(S)->fail; preguntar(S))).
limpiar :- retract(si(_)),fail.
limpiar :- retract(no(_)),fail.
limpiar.

% proceso de eleccion de acuerdo al diagnostico basado en las preguntas
% anteriores

botones :- lim,
	send(@boton,free),
	send(@btncarrera,free),
	fallas(Falla),
	send(@texto,selection(' ')),
	send(@respl,selection(Falla)),
	new(@boton,button('inicia procedimiento mecanico',message(@prolog,botones))),
        send(Menu,display,@boton,point(40,50)),
        send(Menu,display,@btncarrera,point(20,50)),
limpiar.
lim :- send(@respl, selection('')).










































