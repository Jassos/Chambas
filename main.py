from bs4 import BeautifulSoup
import re

def scrape_jobs(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    jobs = []
    
    # Encontrar todos los elementos de trabajo
    job_cards = soup.find_all('div', class_='cardOutline')
    
    for job in job_cards:
        job_data = {}
        
        # Título del trabajo
        title_elem = job.find('h2', class_='jobTitle')
        if title_elem:
            job_data['title'] = title_elem.get_text(strip=True)
        
        # Nombre de la empresa
        company_elem = job.find('span', attrs={'data-testid': 'company-name'})
        if company_elem:
            job_data['company'] = company_elem.get_text(strip=True)
        
        # Ubicación
        location_elem = job.find('div', attrs={'data-testid': 'text-location'})
        if location_elem:
            job_data['location'] = location_elem.get_text(strip=True)
        
        # Salario
        salary_elem = job.find('div', attrs={'data-testid': 'attribute_snippet_testid'}, 
                             string=re.compile(r'\$'))
        if salary_elem:
            job_data['salary'] = salary_elem.get_text(strip=True)
        else:
            job_data['salary'] = "No especificado"
        
        # Requisitos (extraídos del snippet)
        requirements = []
        snippet_elem = job.find('div', attrs={'data-testid': 'belowJobSnippet'})
        if snippet_elem:
            for li in snippet_elem.find_all('li'):
                requirements.append(li.get_text(strip=True))
        job_data['requirements'] = requirements if requirements else ["No especificados"]
        
        # Enlace del trabajo
        link_elem = job.find('a', class_='jcs-JobTitle')
        if link_elem and 'href' in link_elem.attrs:
            job_data['link'] = "https://mx.indeed.com" + link_elem['href'] if not link_elem['href'].startswith('http') else link_elem['href']
        
        jobs.append(job_data)
    
    return jobs

# Ejemplo de uso (puedes reemplazar esto con tu código HTML)
if __name__ == "__main__":
    # Aquí puedes pegar tu código HTML o leerlo desde un archivo
    with open('indeed_jobs.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    jobs = scrape_jobs(html_content)
    
    # Imprimir resultados
    for i, job in enumerate(jobs, 1):
        print(f"\nTrabajo #{i}")
        print(f"Título: {job.get('title', 'N/A')}")
        print(f"Empresa: {job.get('company', 'N/A')}")
        print(f"Ubicación: {job.get('location', 'N/A')}")
        print(f"Salario: {job.get('salary', 'N/A')}")
        print("Requisitos destacados:")
        for req in job.get('requirements', []):
            print(f"- {req}")
        print(f"Enlace: {job.get('link', 'N/A')}")