from django.shortcuts import render, redirect
from .forms import ClienteForm,CitaForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Cliente
from .forms import BuscadorClienteForm

def pagina_inicio(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # 1. Obtener datos limpios
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # 2. 🏆 VERIFICACIÓN SECRETA (La función clave)
            # Django busca el usuario y compara la contraseña ingresada con el hash guardado.
            # Si coinciden, devuelve el objeto User; si no, devuelve None.
            user = authenticate(request, username=username, password=password) 

            if user is not None:
                # 3. 🔑 INICIAR SESIÓN (Crear la sesión de Django)
                # Esta función almacena la ID del usuario en la sesión del navegador.
                login(request, user) 
                
                # Redirigir a la página principal después del login
                return redirect('menu') 
            else:
                # Contraseña o usuario incorrecto
                # Puedes añadir un mensaje de error al request si lo deseas
                return render(request, 'prueba.html', {'form': form, 'error': 'Usuario o contraseña incorrectos.'})
    
    else:
        # Petición GET: Mostrar el formulario vacío
        form = AuthenticationForm()
    
    return render(request, 'principal.html', {'form': form})




def registrar_usuario(request):
    if request.method == 'POST':
        # 1. Instanciar el formulario de creación de usuario
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 2. 🏆 LÓGICA MÁS FÁCIL
            # El método save() del UserCreationForm llama automáticamente a create_user() 
            # y hashea la contraseña de forma segura.
            form.save() 
            return redirect('prueba')
    else:
        form = UserCreationForm()
    
    return render(request, 'crear_usuario.html', {'form': form})
    
    

def nuevo_cliente(request):
    # 1. Caso GET (Mostrar formulario vacío)
    if request.method == 'GET':
        form = ClienteForm()
        return render(request, 'nuevo_usuario.html', {'form': form})

    # 2. Caso POST (Procesar datos)
    elif request.method == 'POST':
        # Instanciar el formulario con los datos POST
        form =ClienteForm(request.POST)

        # Verificar la validez
        if form.is_valid():
            # Si es válido, guardar y redirigir
            form.save()
            return redirect('menu')
        else:
            # Si NO es válido, SIMPLEMENTE renderizar el template
            # usando el objeto 'form' existente, que ya contiene 
            # los datos incompletos/incorrectos y los errores de validación.
            print(form.errors) # Puedes imprimir los errores para debug
            return render(request, 'nuevo_usuario.html', {'form': form})
        
def crear_cita(request):
    
    form = CitaForm(request.POST) 
    if form.is_valid():
        form.save()
        return redirect('menu')
    else:
        
          print("--- ERRORES DE CitaForm ---")
          print(form.errors)
    return render(request, 'cita.html', {'form': form})

def menu(request):
    return render(request, 'menu.html')

############

def cliente_busqueda(request):
    form = BuscadorClienteForm(request.GET) # Recibimos los datos por GET
    clientes = Cliente.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            # Filtramos por nombre o teléfono
            clientes = clientes.filter(
                Q(nombre__icontains=query) | Q(apellido__icontains=query) |Q(telefono__icontains=query)
            )

    return render(request, 'cliente_busqueda.html', {
        'clientes': clientes,
        'form': form
    })


#preparando la busqueda de clientes
def lista_clientes(request):
    busqueda = request.GET.get('buscar') # Obtenemos lo que el usuario escribió
    clientes = Cliente.objects.all()

    if busqueda:
        # Filtramos: que el nombre CONTENGA la búsqueda O el teléfono CONTENGA la búsqueda
        clientes = clientes.filter(
            Q(nombre__icontains=busqueda) | 
            Q(telefono__icontains=busqueda)
        )

    return render(request, 'lista_clientes.html', {'clientes': clientes})





# Create your views here.
